const express = require('express');
const bodyParser = require('body-parser');
const { graphqlHTTP } = require('express-graphql');
const { buildSchema } = require('graphql');
const mongoose = require('mongoose');
const bcrypt = require('bcryptjs');

const Event = require('./models/event');
const User = require('./models/users');

const app = express();

app.use(bodyParser.json());

app.use(
  '/graphql',
  graphqlHTTP({  //funktion för att få tag på data, ändra eller ta bort (är som en blueprint för all data som får tas in till databasen)
    schema: buildSchema(`
        type Event {
            _id: ID!
            title: String!
            description: String!
            price: Float!
            date: String!
        }
        
        type User {
          _id: ID!
          email: String!
          password: String
        }

        input EventInput {
            title: String!
            description: String!
            price: Float!
            date: String!
        }

        input UserInput {
          email: String!
          password: String!
        }

        type RootQuery {
            events: [Event!]!
        }

        type RootMutation {
            createEvent(eventInput: EventInput): Event
            createUser(userInput: UserInput): User
        }
        schema {
            query: RootQuery
            mutation: RootMutation
        }
    `),
    rootValue: {
      events: () => { //Skickar ut Events
        return Event.find().then(events => {
          return events.map(event => {
            return {...event._doc, _id: event._doc._id.toString() };
          })
        }).catch(err => {
          console.log(err)
          throw err
        })
      },
      createEvent: args => { //Skapar Events
            const event = new Event({
              title: args.eventInput.title,
              description: args.eventInput.description,
              price: +args.eventInput.price,
              date: new Date(args.eventInput.date),
              creator: '628a413c7021e6603826e2a8' //hårdkodat !!!!!ÄNDRA SEN!!!!!!!!
            });
            let createdEvent;
            return event
            .save().then(result => {
              createdEvent = {...result._doc, _id: result._doc._id.toString() };
              return User.findById('628a413c7021e6603826e2a8') 
            }).then(user => {
              if (!user) {
                throw new Error('User not found!!!')
              }
              user.createdEvents.push(event);
              return user.save();
            }).then(result => {
              return createdEvent
            }).catch(err => {
              console.log(err);
              throw err;
            });
          },
          createUser: args => { //Skaper Användare
             return User.findOne({email: args.userInput.email}).then(user => {
              if (user) {
                throw new Error('Users email taken!!!')
              }
              return bcrypt
            .hash(args.userInput.password, 12)
            }).then(hashpass => {
              const user = new User({
                email: args.userInput.email,
                password: hashpass
              });
              return user.save();
            }).then(result => {
              return {...result._doc, password: null, _id: result._doc._id.toString() };
            }).catch(err => {
              throw(err)
            });
          }
        },
    graphiql: true
  })
);

mongoose.connect(`mongodb+srv://${process.env.MONGO_USER}:${process.env.MONGO_PASSWORD}@cluster0.d2bwv.mongodb.net/${process.env.MONGO_DB}?retryWrites=true&w=majority` //Kopplar sig in på databasen
).then(() => {
  app.listen(3000); //startar servern på port 3000
}).catch(err => {
  console.log(err);
});

