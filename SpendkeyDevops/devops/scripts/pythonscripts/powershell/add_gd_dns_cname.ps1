param
(
	[string] $godaddy_domain,
	[string] $godaddy_name,
	[string] $godaddy_destination,
	#[string] $godaddy_type,
	[string] $godaddy_key,
	[string] $godaddy_secret 
)

#Authenication
$headers = @{}
$headers["Authorization"] = 'sso-key ' + $godaddy_key + ':' + $godaddy_secret

#Get the cname
Write-Host "Check GoDaddy.com for current CNAME details"
$CNameGetResponse = Invoke-WebRequest https://api.goDaddy.com/v1/domains/$godaddy_domain/records/CNAME/$godaddy_name -method get -Headers $headers -ContentType "application/json"

#Set the cname
$results = ConvertFrom-Json -InputObject $CNameGetResponse.Content
if ($results.data.length -eq 0)
{

    [array]$Request=@{"data"=$godaddy_destination; "ttl"=600;} #"port"=65535; "Priority"=0; "Protocol"="none"; "service"="none";  "weight"=0}
    $JSON = ConvertTo-Json $Request

    try{
		Invoke-WebRequest https://api.goDaddy.com/v1/domains/$godaddy_domain/records/CNAME/$godaddy_name -Method Put -Headers $headers -Body $JSON -ContentType "application/json"
    	Write-Host "updated cname record $godaddy_name in GoDaddy.com"
	}
	catch {
		"Error:"+$Error[0]
		#Write-Host ("ERROR: " + $_.ScriptStackTrace + ":" + $_) -ForegroundColor Red
	}
		
    
}

else
{
    Write-Host "No DNS update needed in GoDaddy.com"
}

