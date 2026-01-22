
provider "google" {
  project = var.gcp_project_id
  region  = var.gcp_region
}

resource "google_project_iam_member" "default" {
  project = var.gcp_project_id
  role    = "roles/owner" # This is just an example, use a more specific role in production
  member  = "user:your-email@example.com" # Replace with your GCP user email
}
