const express = require("express");
const bodyParser = require("body-parser");
const { graphqlHTTP } = require("express-graphql");
const mongoose = require("mongoose");
const app = express();
const isAuth = require("./middleware/is-auth");

const graphSchema = require("./graphql/schema/index");
const graphResolvers = require("./graphql/resolvers/index");

app.use(bodyParser.json());

app.use((req, res, next) => {
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Access-Control-Allow-Methods", "POST,GET,OPTIONS");
  res.setHeader("Access-Control-Allow-Headers", "Content-Type, Authorization");
  if (req.method === "OPTIONS") {
    return res.sendStatus(200);
  }
  next();
});

app.use(isAuth);

app.use(
  "/graphql",
  graphqlHTTP({
    schema: graphSchema,
    rootValue: graphResolvers,
    graphiql: true,
  })
);

mongoose
  .connect(
    `mongodb+srv://${process.env.MONGO_USER}:${process.env.MONGO_PASSWORD}@cluster0.d2bwv.mongodb.net/${process.env.MONGO_DB}?retryWrites=true&w=majority` //Kopplar sig in på databasen
  )
  .then(() => {
    app.listen(8000); //startar servern på port 8000
  })
  .catch((err) => {
    console.log(err);
  });
