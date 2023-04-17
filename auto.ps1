git add .

$message = Read-Host "Enter commit message: "

git commit -m "$message" 

git push -u origin main