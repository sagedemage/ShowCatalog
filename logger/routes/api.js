var express = require('express');
var router = express.Router();
const Log = require('../helpers/database');

/* GET home page. */

router.post('/add-log', function(req, res, next) {
	const log = new Log({show_id: req.body.show_id, msg: req.body.msg, method: req.body.method, date: Date.now()})
	log.save()
	res.send('added a document');
});

module.exports = router;
