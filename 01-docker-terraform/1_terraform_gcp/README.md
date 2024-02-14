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

To use variables in terraform, create a file called `variables.tf` in the same directory of `main.tf` and insert the variables for the project. Example:

```
variable "credentials_path" {
  description = "GCP credentials"
  default     = "path/to/your/credentials"
}

variable "project" {
  description = "GCP Project"
  default     = "project-id"
}

variable "region" {
  description = "GCP Project region"
  default     = "region-id
}

variable "location" {
  description = "Project location"
  default     = "location"
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  default     = "dataset-name"
}

variable "gcs_bucket_name" {
  description = "GCS bucket name"
  default     = "bucket-name"
}

variable "gcs_storage_class" {
  description = "GCS bucket class"
  default     = "gcs-class"
}
```

Also, update the `main.tf` file with the variables call:
```

(...)

provider "google" {
  project     = var.project
  region      = var.region
  credentials = file(var.credentials_path)
}

resource "google_storage_bucket" "demo-bucket" {
  name          = var.gcs_bucket_name
  location      = var.location
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 7
    }
    action {
      type = "Delete"
    }
  }
}

(...)

```