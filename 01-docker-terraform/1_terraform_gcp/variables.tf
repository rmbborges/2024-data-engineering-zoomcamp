variable "credentials_path" {
  description = "GCP credentials"
  default     = ""
}

variable "project" {
  description = "GCP Project"
  default     = ""
}

variable "region" {
  description = "GCP Project region"
  default     = ""
}

variable "location" {
  description = "Project location"
  default     = ""
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  default     = ""
}

variable "gcs_bucket_name" {
  description = "GCS bucket name"
  default     = ""
}

variable "gcs_storage_class" {
  description = "GCS bucket class"
  default     = ""
}
