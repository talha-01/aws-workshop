
# A template for a secure static website leveraging s3, CloudFront and Route53, and restricting access to s3 bucket with OAI.

## The modifications you need to do:

- Find your Original Access Idendity.

![OAI](OAI.png)

- Change the XXXXXXXXXXXX in the bucket policy with your OAI.

![bucket-policy](bucket-policy.png)

- Change the XXXXXXXXXXXX in the CloudFormation origins configuration with your OAI.

![origins-configuration](origins-configuration.png)

