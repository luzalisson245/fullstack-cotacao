const express = require('express');
const bodyParser = require('body-parser');
const app = express();

app.use(bodyParser.json());

const port = process.env.PORT || 3001;

app.listen(port, function() {
  console.log('Server listening on port ' + port);
});
