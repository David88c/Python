# Create remote computer connection using New-CimSession
$session = New-CimSession -ComputerName "HQPLMSOLID01"

# Loop until the task status is "Ready"
while ((Get-ScheduledTask -TaskName "qs_batch_no_gui").State -eq "Running") {
    Write-Host "Task is still running. Waiting..."
    Start-Sleep -Seconds 10
}

# Disable the scheduled tasks on remote computer
Disable-ScheduledTask -CimSession $session -TaskName "qs_batch_no_gui"

Start-Sleep -Seconds 5

# Create remote computer connection using New-CimSession
$session = New-CimSession -ComputerName "HQPLMFTSPRD01"

# Loop until the task status is "Ready"
while ((Get-ScheduledTask -TaskName "FTS_indexing_task").State -eq "Running") {
    Write-Host "Task is still running. Waiting..."
    Start-Sleep -Seconds 10
}

# Disable the scheduled tasks on remote computer
Disable-ScheduledTask -CimSession $session -TaskName "FTS_indexing_task"

Stop-Service -Name "3DEXPERIENCE R2017x Full-text AdvancedSearch"

Start-Sleep -Seconds 5

# Create remote computer connection using New-CimSession
$session = New-CimSession -ComputerName "HQPLMPRD01"

Stop-Service -Name "3DPassport_R2017x", "3DSpaceTomEE_R2017x", "3DDashboard_R2017x", "federated_R2017x", "Apache2.4"

Start-Sleep -Seconds 5

# Create remote computer connection using New-CimSession
$session = New-CimSession -ComputerName "HQPLMFCSPRD01"

Stop-Service -Name "TomEE", "Apache2.4", "3DEXPERIENCE R2017x AdvancedSearchFileConverter"

# List of servers to restart
$Servers_list = "HQPLMPRD01", "HQPLMFTSPRD01", "HQPLMFCSPRD01", "HQPLMSOLID01"

# Restart the servers
foreach ($server in $Servers_list) {
    Restart-Computer -ComputerName $server -Force
    Write-Host "Restarting $server..."
}

# Wait for servers to come back online
Start-Sleep -Seconds 600

# Create remote computer connection using New-CimSession
$session = New-CimSession -ComputerName "HQPLMFTSPRD01"

# Enable the scheduled tasks on remote computer
Enable-ScheduledTask -CimSession $session -TaskName "FTS_indexing_task"

# Create remote computer connection using New-CimSession
$session = New-CimSession -ComputerName "HQPLMSOLID01"

# Enable the scheduled tasks on remote computer
Enable-ScheduledTask -CimSession $session -TaskName "qs_batch_no_gui"