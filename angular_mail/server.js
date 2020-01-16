var nodemailer = require('nodemailer');

var transporter = nodemailer.createTransport({
    service: 'hotmail',
    auth: {
      user: 'gonzaromero_2007@hotmail.com',
      pass: ''
    }
  });
  
  var mailOptions = {
    from: 'gonzaromero_2007@hotmail.com',
    to: 'gonzaromero2007@gmail.com',
    subject: 'Sending Email using Node.js',
    text: 'That was easy!'
  };
  
  transporter.sendMail(mailOptions, function(error, info){
    if (error) {
      console.log(error);
    } else {
      console.log('Email sent: ' + info.response);
    }
  }); 