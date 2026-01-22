
output "project_id" {
  description = "The ID of the GCP project."
  value       = google_project_iam_member.default.project
}
