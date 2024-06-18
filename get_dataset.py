import pandas as pd  

service_account_info = {
  "type": "service_account",
  "project_id": "alert-howl-193320",
  "private_key_id": "3361cd7171aecac8b4ab2dfa4ccf3d0825015f34",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDGawdc1CeSGiJy\nVoe+yv2gz7rpKLuEgLSGWGE6rSz8wXssvLoPNppY2rh4l9VJXyHmR7BA9kxa+eZo\nG9RpozaTGtvWsyebk97ilWMBnTE5k//R8xVclJDK8Y9i6ZluYzFn9kRR9RufJwKr\nq88OO3IRlsXjOkLo3vHsIOdO+hfrHknQoqe2fpm80Ner2jyOh50Xb70lJsaijagx\nSk3ak0Vv2j0xR1wx6Cl04bAx48wFgxCoSquYeluNrHEJ4/05y9XozbpM3GOnAFsz\n07vs32WPWwVY15/6SSRWuIIJNafmTgtfzbM5rOAH3MeLQVRG22RnkAozx9/+FvfX\n9BL4Ra2DAgMBAAECggEAYBFkEDL8McYLlZaFxP/diyXo1okNOZtjTISwFsvQM1Su\ngbuizkjetFS56lGBSDQSYr+k+98EmyvRvehzkO4gN1tSw4IclDwlN0mjFR35vmoE\n+68ZUajw7gHFLdvymLrYKgDXlWL6i7VEmr/l0XtAwHliuKD10nBXa7+GnvuB5yj4\niDhi+pK4XRRwGHWLbldIC919yrVYsERJoTUt0EjcLsE9g7otoO+DkBNqx+JaFm7m\nvDBNsP/DQ1jFHN6eUFDbBBJaH6R6HtXPDTtVxp+txLNvd9oRMXn352ad3bnzr9yX\n+cKWZRXclWA0d4EZXhOScBqtq9Vj8TF8dUFeWnFpIQKBgQD7IdpWel7013ideJoK\nA1ZqVzijphG85P0clTekJQGj/3dY5zjN11bMDOgbRnW+YliHo1ddW508zt2d5sl+\nLQZbxxUdibXQ/AcDXCb6ucYpewOGafaCnXdNAyyN/eDYc7fBUhD0fGX1JA+xQAQ1\nSNJelm52irTc9XOEToK7cW1WsQKBgQDKQ5om0plU4X91sXFETUpFGIujETi4BD87\nClhs2ZYUjcQRBH2TEIEMNwUBxKvHx6QPN/7FXV+XPMMv76QbjMxbM0YUexFjhFqa\nA7CSGZnAfEciB6Srk+W7uS5O1jTHG2NHGyZHaz/aUQ6n0MXSwACUYs+TyRALcZr9\nsTwQr0p8cwKBgDBIOeoWbNs18gKUhUkXiy22xzTvYMmoXOF57tCoLMCTBScajVlF\n5XIlqRpVWZ3Y2px5Uvqn+nsOap1JGcQgc/CBPhYHu+UKD28d8ICT5v1ioTLefH5w\nN9eenJpQDUKQPOv2EzxuDkwrOrkhTa3Q6mE1Gte/ozY4GpV9YrUXAaaBAoGAIrbX\njjI2/sp1Bc4ekopxZMqBrMsX4P1ZnNh5tLTjfUOXkxQiOUtr2pzWzybiFLe/AJ2r\nrFQKQ/q5xVBr6g6QRFbYgEtfAKWGp0ha1bhvGwo5ay3EpW4Mz9tIh19cT4/zyhBu\n0XMm0mF3EnZSfYlWkCElX0fy6QPmhgQVOwfa0OECgYEA48LNSRX8Mr+B1+1Y1bWd\nJo1rauD6y9l1aX2Ej6vpuAXMRNhuoCLAZYD5kPSvm9UY4HV+SjC8L/VPF9lvGl62\novANxMGjCIpddIZYLbv/hfRbRXQ5C32YzGQq8v3JyQnhtQHu22I2vuH8HZaiLQ55\njJiG+sWwtpKKegDctYFURnQ=\n-----END PRIVATE KEY-----\n",
  "client_email": "storage-only@alert-howl-193320.iam.gserviceaccount.com",
  "client_id": "112832242348266519653",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/storage-only%40alert-howl-193320.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}

def get_dataframe(start_date: str = '2020-01-01', 
                  end_date: str = '2021-12-31'): 

    df_proce = pd.read_parquet('gs://sovai-text/processed_df',
                            filters=[('date', '>=', start_date), ('date', '<=', end_date)],
                             storage_options={'token': service_account_info}) #columns=['DATE', 'url', 'title'],

    return df_proce

