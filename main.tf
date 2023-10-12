resource "aws_db_instance" "source_db" {
}

resource "aws_dms_replication_instance" "dms_instance" {
}

resource "aws_dms_endpoint" "source_endpoint" {
}

resource "aws_dms_replication_task" "dms_task_to_sqs" {
}

resource "aws_sqs_queue" "dms_sqs" {
}

resource "aws_lambda_function" "dms_lambda" {
}

resource "aws_db_instance" "destination_db" {
}

resource "aws_lambda_event_source_mapping" "lambda_sqs_mapping" {
  function_name    = aws_lambda_function.dms_lambda.function_name
  event_source_arn = aws_sqs_queue.dms_sqs.arn
}

