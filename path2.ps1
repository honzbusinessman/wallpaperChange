$url      = 'https://www.callums-corner.com/wp-content/uploads/2017/08/self-defence-video.jpg'
$req      = Invoke-WebRequest -Uri $url -OutFile 'C:\image.jpg'

$regPath  = 'HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System'
$keyName  = 'Wallpaper'
$keyValue = 'C:\image.jpg'

Set-ItemProperty -Path $regPath -Name $keyName -Value $keyValue