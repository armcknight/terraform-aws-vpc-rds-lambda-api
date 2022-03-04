# Learn Terraform - Lambda functions and API Gateway

AWS Lambda functions and API gateway are often used to create serverlesss
applications.

Follow along with this [tutorial on HashiCorp
Learn](https://learn.hashicorp.com/tutorials/terraform/lambda-api-gateway?in=terraform/aws).

## Extra info/steps

- After running `terraform apply` to export/upload the lambda to the S3 bucket, check that it's there with:

```shell
aws s3 ls $(terraform output -raw lambda_bucket_name) --profile armcknight
```

- After creating the lambda function, invoke it with:

```shell
aws lambda invoke --region=us-east-1 --function-name=$(terraform output -raw function_name) response.json
```