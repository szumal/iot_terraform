provider "aws" {
  region = var.aws_region
}

resource "aws_iot_thing" "device" {
  name = "gg-demo-device"
}

resource "aws_iot_certificate" "cert" {
  active = true
}

resource "aws_iot_policy" "policy" {
  name   = "gg-demo-policy"
  policy = jsonencode({
    Version: "2012-10-17",
    Statement : [
      {
        Effect : "Allow",
        Action = [
          "iot:*",
          "greengrass:*"
        ],
        Resource : ["*"]
      }
    ]
  })
}

resource "aws_iot_policy_attachment" "cert_policy" {
  policy = aws_iot_policy.policy.name
  target = aws_iot_certificate.cert.arn
}

resource "aws_iot_thing_principal_attachment" "cert_attach" {
  thing       = aws_iot_thing.device.name
  principal   = aws_iot_certificate.cert.arn
}
