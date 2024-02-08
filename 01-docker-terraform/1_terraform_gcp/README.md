## How to reproduce the code in this section

Export the path to a SA credential:
```
export GOOGLE_APPLICATION_CREDENTIALS='/complete/path/to/your/credentials'
echo $GOOGLE_APPLICATION_CREDENTIALS
```

Edit the main.tf file with the project and bucket name in "google_storage_bucket" "demo-bucket" resource:
```
provider "google" {
  project = "project-id"
  region  = "region"
}

(...)

resource "google_storage_bucket" "demo-bucket" {
  name          = "bucket-name"
  location      = "bucket-region"

(...)

}

```

Execute `terraform init` to pull the provider extesion;

Execute `terraform plan` to check for the creation plan of the provider resources;

Finally, execute `terraform apply` to execute the creation plan, generating the `terraform.tfstate` file, that contains the logs of what was created;

To delete the resources, execute `terraform destroy`. It will destroy every resource mapped in `terraform.tfstate` file.