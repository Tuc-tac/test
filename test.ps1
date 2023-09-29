[Net.ServicePointManager]::SecurityProtocol = 3072

iex "& { $(iwr -useb 'https://spotx-official.github.io/SpotX/run.ps1') } $args"
