$url      = 'https://grmdaily.com/wp-content/uploads/2020/10/callums-corner.png'
$req      = Invoke-WebRequest -Uri $url -OutFile 'C:\image.jpg'

$regPath  = 'HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System'
$keyName  = 'Wallpaper'
$keyValue = 'C:\image.jpg'

Set-ItemProperty -Path $regPath -Name $keyName -Value $keyValue
