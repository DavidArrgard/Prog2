const Event = require("../../models/event");
const User = require("../../models/users");
const { dateToString } = require("../../helpers/date");

const events = async (eventsIds) => {
  try {
    const events = await Event.find({ _id: { $in: eventsIds } });
    return events.map((event) => {
      return eventTransformer(event);
    });
  } catch (err) {
    throw err;
  }
};

const user = async (userId) => {
  try {
    const user = await User.findById(userId);
    return {
      ...user._doc,
      _id: user.id,
      createdEvents: events.bind(this, user._doc.createdEvents),
    };
  } catch (err) {
    throw err;
  }
};

const singleEvent = async (eventId) => {
  try {
    const event = await Event.findById(eventId);
    return eventTransformer(event);
  } catch (err) {
    throw err;
  }
};

const eventTransformer = (event) => {
  return {
    ...event._doc,
    _id: event.id,
    date: dateToString(event._doc.date),
    creator: user.bind(this, event._doc.creator),
  };
};

const bookingTransformer = (booking) => {
  return {
    ...booking._doc,
    _id: booking.id,
    user: user.bind(this, booking._doc.user),
    event: singleEvent.bind(this, booking._doc.event),
    createdAt: dateToString(booking._doc.createdAt),
    updatedAt: dateToString(booking._doc.updatedAt),
  };
};

exports.eventTransformer = eventTransformer;
exports.bookingTransformer = bookingTransformer;

// exports.user = user;
// exports.events = events;
// exports.singleEvent = singleEvent;
