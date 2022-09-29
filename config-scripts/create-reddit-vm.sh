SVC_ACCT="packer"
FOLDER_ID="b1gl0ur70v6b2cqcn4aa"
yc iam service-account create --name $SVC_ACCT --folder-id $FOLDER_ID
ACCT_ID=$(yc iam service-account get $SVC_ACCT | \
grep ^id | \
awk '{print $2}')
yc resource-manager folder add-access-binding --id $FOLDER_ID --role editor --service-account-id $ACCT_ID
yc iam key create --service-account-id $ACCT_ID --output script/key.json
packer build ./variables.json
