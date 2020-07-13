## Send Email by Python Code

This Python code sends an email to the user. The `input.json` file includes the following parameters,


`name`: User name  
`email`: User email address  
`wd_email`: Watchdog email address  
`wd_key`: Watchdog email password (encoded `wd_key_iter` times by `base64` module)  
`wd_key_iter`: Number of encodings for real `wd_key`  
`smtp`: smtp host address (default: smtp.gmail.com)  
`smtp_port`: smtp port number (default: 465)  
`ssl`: Flag to activate secure socket layer for strong encryption  


### Warning:  
This is not a secure way of passing email password when using unsecured or public networks. Update the algorithm as desired.
Read `wd_key` from OS ENV variables. Always better!

