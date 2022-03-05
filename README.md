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

- After adding a query parameter to the lambda function and API gateway endpoint, do it this way:

```shell
curl "$(terraform output -raw base_url)/hello?Name=Terraform"
```

## TODO

- Set up DNS to allow a URL like https://something.mcknight.rocks/something instead of the default API gateway URL (e.g. https://6e074kbkl4.execute-api.us-east-1.amazonaws.com/serverless_lambda_stage)
- set up RDS-managed database and do some simple record insertions from the lambda (maybe the number of times it has been called so far, returning the current count in the HTTP response and incrementing it in the db)

## Other references

More about lambda + api gateways:
- _Tutorial: Using Lambda with API Gateway_: https://docs.aws.amazon.com/lambda/latest/dg/services-apigateway-tutorial.html

More about RDS:
- _Tutorial: Configuring a Lambda function to access Amazon RDS in an Amazon VPC_: https://docs.aws.amazon.com/lambda/latest/dg/services-rds-tutorial.html
- _Manage AWS RDS Instances_: https://learn.hashicorp.com/tutorials/terraform/aws-rds?in=terraform/aws