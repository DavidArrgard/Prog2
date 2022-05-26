const Event = require("../../models/event");
const User = require("../../models/users");
const { eventTransformer } = require("./merge");

module.exports = {
  events: async () => {
    //Skickar ut Events
    try {
      const events = await Event.find();
      return events.map((event) => {
        return eventTransformer(event);
      });
    } catch (err) {
      throw err;
    }
  },
  createEvent: async (args, req) => {
    //Skapar Events
    if (!req.isAuth) {
      throw new Error("Unauthenticated");
    }
    const event = new Event({
      title: args.eventInput.title,
      description: args.eventInput.description,
      price: +args.eventInput.price,
      date: new Date(args.eventInput.date),
      creator: req.userId,
    });
    let createdEvent;
    try {
      const result = await event.save();
      createdEvent = eventTransformer(result);
      const creator = await User.findById(req.userId);
      if (!creator) {
        throw new Error("User not found!!!");
      }
      creator.createdEvents.push(event);
      await creator.save();

      return createdEvent;
    } catch (err) {
      console.log(err);
      throw err;
    }
  },
};
