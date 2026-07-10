Remove-Item Alias:gc -Force
Remove-Item Alias:gp -Force
Remove-Item Alias:gl -Force
function rs {
    python manage.py runserver
}

function mm {
    python manage.py makemigrations
}

function mig {
    python manage.py migrate
}

function sh {
    python manage.py shell
}

function gs { git status }
function ga { git add . }
function gc { git commit -m $args }
function gp { git push }
function gl { git pull }
function gb { git branch }
function gco { git checkout $args }
# Import the Chocolatey Profile that contains the necessary code to enable
# tab-completions to function for `choco`.
# Be aware that if you are missing these lines from your profile, tab completion
# for `choco` will not function.
# See https://ch0.co/tab-completion for details.
$ChocolateyProfile = "$env:ChocolateyInstall\helpers\chocolateyProfile.psm1"
if (Test-Path($ChocolateyProfile)) {
  Import-Module "$ChocolateyProfile"
}
