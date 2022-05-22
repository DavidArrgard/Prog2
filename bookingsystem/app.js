const express = require("express");
const bodyParser = require("body-parser");
const { graphqlHTTP } = require("express-graphql");
const mongoose = require("mongoose");
const app = express();

const graphSchema = require("./graphql/schema/index");
const graphResolvers = require("./graphql/resolvers/index");

app.use(bodyParser.json());

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
    app.listen(3000); //startar servern på port 3000
  })
  .catch((err) => {
    console.log(err);
  });
