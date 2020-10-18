const express = require('express');
const router = express.Router();
const { insert } = require('../utils/mongodb')

router.use(express.json({ limit:"1GB"}));

router.post('/', async (req, res, next) => {
    const data = req.body;
    console.log(data);
    await insert(data)
    res.sendStatus(200)
});

module.exports = router;
