# 1- creating the private key (without passphrase)
openssl genrsa -out key.pem 2048
# with passphrase
openssl genrsa -aes256 -out key.pem 2048

# 2- generate CSR
openssl req -new -key key.pem -out signreq.csr

# 3- signing the certificate with the key
openssl x509 -req -days 365 -in signreq.csr -signkey key.pem -out certificate.pem

# (Optional) view the certificate
openssl x509 -text -noout -in certificate.pem
