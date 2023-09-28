# Get information about the processor
$processor = Get-WmiObject -Class Win32_Processor
$processorName = $processor.Name
$numberOfCores = $processor.NumberOfCores
$cpuSpeed = $processor.MaxClockSpeed

# Get information about physical memory (RAM)
$memory = Get-WmiObject -Class Win32_PhysicalMemory
$totalRAM = [math]::Round(($memory | Measure-Object -Property Capacity -Sum).Sum / 1GB)

# Display information on the screen
Write-Host "Processor Information:"
Write-Host "Processor Model: $processorName"
Write-Host "Number of Cores: $numberOfCores"
Write-Host "CPU Speed (MHz): $cpuSpeed"

Write-Host "Memory Information:"
Write-Host "Total RAM (GB): $totalRAM"
