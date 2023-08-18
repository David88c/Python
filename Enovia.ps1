# Get the current date in the desired format
$dateString = Get-Date -Format "ddMMyyy"

# Define the parent directory where you want to create the folder
$parentDirectory = "D:\LOGS"

# Create the folder with the date-based name
$newFolderName = "$dateString"
$newFolderPath = Join-Path -Path $parentDirectory -ChildPath $newFolderName
$batchFilePath = "D:\ContEnoMonSvr\Run_MONITOR_DB_LOCKS.bat"

if (-not (Test-Path -Path $newFolderPath -PathType Container)) {
    New-Item -Path $newFolderPath -ItemType Directory
    Write-Host "Folder '$newFolderName' created successfully."
} else {
    Write-Host "Folder '$newFolderName' already exists."
}

# Define paths
$logFilePath01 = "D:\R2017x\3DSpace\win_b64\code\tomcat\current\logs\*"
$logFilePath02 = "D:\R2017x\3DSpace\logs\*"
$serviceName = "3DEXPERIENCE R2017x 3DSpace TomEE"


# Copy the log file to the destination path
Copy-Item -Path $logFilePath01 -Destination $newFolderPath
Copy-Item -Path $logFilePath02 -Destination $newFolderPath

sleep 5

# Run the batch file
#Start-Process -FilePath $batchFilePath -Wait

sleep 5

# Define source and destination paths
$DB_locks_dir = "D:\ContEnoMonSvr\Logs\LOCKS"


# Get the latest created file in the source directory
$latestFile = Get-ChildItem -Path $DB_locks_dir | Sort-Object CreationTime -Descending | Select-Object -First 1

if ($latestFile) {
    # Create the destination directory if it doesn't exist
    if (-not (Test-Path -Path $newFolderpath -PathType Container)) {
        New-Item -Path $newFolderpath -ItemType Directory
    }

    # Copy the latest file to the destination directory
    $destinationPath = Join-Path -Path $newFolderpath -ChildPath $latestFile.Name
    Copy-Item -Path $latestFile.FullName -Destination $destinationPath -Force
    Write-Host "Latest file '$($latestFile.Name)' copied to '$destinationPath'."
} else {
    Write-Host "No files found in the source directory."
}

#Restart the specified service
#Restart-Service -Name $serviceName