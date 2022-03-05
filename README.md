# Terraform AWS VPC+RDS+API+Lambda test

- Set up the Lambda and API gateway:
    - _Deploy Serverless Applications with AWS Lambda and API Gateway_: https://learn.hashicorp.com/tutorials/terraform/lambda-api-gateway?in=terraform/aws ([cached PDF](https://github.com/armcknight/learn-terraform-lambda-api-gateway/blob/main/docs/Deploy%20Serverless%20Applications%20with%20AWS%20Lambda%20and%20API%20Gateway%20%7C%20Terraform%20-%20HashiCorp%20Learn.pdf))
- Set up the VPC:
    - _Building an AWS VPC with Terraform Step-by-Step_: https://adamtheautomator.com/terraform-vpc/ ([cached PDF](https://github.com/armcknight/learn-terraform-lambda-api-gateway/blob/main/docs/Building%20an%20AWS%20VPC%20with%20Terraform%20Step-by-Step.pdf))
    - _Deploy AWS RDS + AWS Lambda + AWS API Gateway + corresponding VPC, subnets and security group with Terraform_: https://github.com/chromium58/terraform-aws-example/tree/61dbd8371d9508e3510e20ef24f9286d10de5f49

## TODO

- Set up a VPC to contain the various infra components
- Set up DNS to allow a URL like https://something.mcknight.rocks/something instead of the default API gateway URL (e.g. https://6e074kbkl4.execute-api.us-east-1.amazonaws.com/serverless_lambda_stage)
- set up RDS-managed database and do some simple record insertions from the lambda (maybe the number of times it has been called so far, returning the current count in the HTTP response and incrementing it in the db)

## Other references

More about lambda + api gateways:
- _Tutorial: Using Lambda with API Gateway_: https://docs.aws.amazon.com/lambda/latest/dg/services-apigateway-tutorial.html

More about RDS:
- _Tutorial: Configuring a Lambda function to access Amazon RDS in an Amazon VPC_: https://docs.aws.amazon.com/lambda/latest/dg/services-rds-tutorial.html
- _Manage AWS RDS Instances_: https://learn.hashicorp.com/tutorials/terraform/aws-rds?in=terraform/aws

Terraform docs:
- `aws`: https://registry.terraform.io/providers/hashicorp/aws/latest/docs
- `aws_vpc`: https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/vpc
- `aws_rds`:
- `aws_lambda`: https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lambda_function
- `aws_apigatewayv2_api` (HTTP APIs): https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/apigatewayv2_api
