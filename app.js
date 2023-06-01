const express = require("express");
const mongoose = require("mongoose");
const dotenv = require("dotenv");
const bodyparser = require("body-parser");
var cors = require("cors");


const app = express();
app.use(express.json());
app.use(bodyparser.json())
app.use(cors());

dotenv.config({ path: "./config.env" });



mongoose.connect(process.env.DB_URI).then((data) => {
    console.log(`Mongodb connected with server: ${data.connection.host}`);
}).catch((err) => {
    console.log(err, "error");
});

const infoSchema = new mongoose.Schema({
    name: { type: String, default: "" },
    email: { type: String, default: "" },
    phone: { type: Number, default: "" }
})

const Info = mongoose.model("info", infoSchema);

app.get("/", (req, res) => {
    res.json({
        result: "helo"
    })
})

app.post("/createRow", async (req, res, next) => {

    console.log(req.body);
    const { name, email, phone } = req.body
    try {
        const result = await Info.create({
            name: name,
            email: email,
            phone: phone
        });
        res.status(200).json({
            success: true,
            result
        })
    } catch (error) {
        res.json({
            success: false,
            error: error.message
        })
    }
});

app.get("/getData", async (req, res, next) => {
    try {
        const result = await Info.find({});
        res.status(200).json({
            success: true,
            result
        })
    } catch (error) {
        res.json({
            success: false,
            error: error.message
        })
    }
});

app.post("/updateData", async (req, res, next) => {
    try {
        const result = await Info.findOneAndUpdate({ _id: req.body.id }, { name: req.body.name, email: req.body.email, phone: req.body.phone }, { new: true })
        res.status(200).json({
            success: true,
            result
        })
    } catch (error) {
        res.json({
            success: false,
            error: error.message
        })
    }
});


app.get("/deleteData", async (req, res, next) => {
    try {
        const result = await Info.findOneAndDelete({ _id: req.query.id });
        res.status(200).json({
            success: true,
            result
        })
    } catch (error) {
        res.json({
            success: false,
            error: error.message
        })

    }
})

let PORT= process.env.PORT || 4000;
app.listen(PORT, () => {
    console.log(`server listening on port ${PORT}`)
})