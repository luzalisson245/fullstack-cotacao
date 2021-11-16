const express = require('express');
const bodyParser = require('body-parser');
const app = express();

app.use(bodyParser.json());

const port = process.env.PORT || 3001;

fetch("http://api.currencylayer.com/live?access_key=1b7f85ec8ad1184e690bd72f54828a40")
 .then(write.resp);

app.listen(port, function() {
  console.log('Server listening on port ' + port);
});