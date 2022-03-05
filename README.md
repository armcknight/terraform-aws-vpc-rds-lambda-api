# Learn Terraform - Lambda functions and API Gateway

Original instructions at: https://learn.hashicorp.com/tutorials/terraform/lambda-api-gateway?in=terraform/aws.

## Extra info/steps

- After running `terraform apply` to export/upload the lambda to the S3 bucket, check that it's there with:

```shell
aws s3 ls $(terraform output -raw lambda_bucket_name) --profile armcknight
```

- After creating the lambda function, invoke it with:

```shell
aws lambda invoke --function-name=$(terraform output -raw function_name) response.json --region=us-east-1 --profile=armcknight
```

and then `cat response.json` to make sure the expected response was received.

- After creating the API gateway, query the endpoint to cause the lambda function to be executed:

```shell
curl "$(terraform output -raw base_url)/hello"
```

## Other references

- _Tutorial: Using Lambda with API Gateway_: https://docs.aws.amazon.com/lambda/latest/dg/services-apigateway-tutorial.html
- _Tutorial: Configuring a Lambda function to access Amazon RDS in an Amazon VPC_: https://docs.aws.amazon.com/lambda/latest/dg/services-rds-tutorial.html
