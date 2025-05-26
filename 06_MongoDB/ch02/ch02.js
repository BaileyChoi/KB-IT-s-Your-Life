// 기본 CRUD
use tutorial;

db.users.insert({ username: "smith" });
db.users.find();

db.users.insert({ username: "jones" });
db.users.count();
db.users.find();

db.users.find({ username: "jones" });

db.users.find({ _id: ObjectId("6833c9df70ee3d354b44152f"), username: "smith" });
db.users.find({ $and: [{ _id: ObjectId("6833c9df70ee3d354b44152f") }, { username: "smith" }] });
db.users.find({
    $or: [
        { username: "smith" },
        { username: "jones" }
    ]
})

db.users.find({ username: "smith" });
db.users.update({ username: "smith" }, { $set: { country: "Canada" } });
db.users.find({ username: "smith" });

db.users.replaceOne({ username: "smith" }, { country: "Canada" });
db.users.find({ country: "Canada" });

db.users.update({ username: "smith" }, { $unset: { country: 1 } });
db.users.find({ username: "smith" });

db.users.find();

db.users.update({ username: "smith" },
    {
        $set: {
            favorites: {
                cities: ["Chicago", "Cheyenne"],
                movies: ["Casabianca", "For a Few Dollars More", "The Sting"]
            }
        }
    });
db.users.update({ username: "jones" },
    {
        $set: {
            favorites: {
                movies: ["Casablanca", "Rocky"]
            }
        }
    });
db.users.find().pretty();

db.users.find({ "favorites.movies": "Casablanca" }).pretty();

db.users.update({ "favorites.movies": "Casablanca" },
    {
        $addToSet: { "favorites.movies": "The Maltese Falcon" }
    },
    {
        upsert: false, // insert if not found?
        multi: true
    }); // update all found? (if false, updates just first it finds)

db.users.remove({ "favories.cities": "Cheyenne" });
db.users.drop();


// 인덱스 생성과 질의
for (let i = 0; i < 20000; i++) {
    db.numbers.insert({ num: i });
}
db.numbers.count();
db.numbers.find({ num: 500 });
db.numbers.find({ num: { "$gt": 19995 } });
db.numbers.find({ num: { "$gt": 20, "$lt": 25 } });

db.numbers.find({ num: { "$gt": 19995 } }).explain("executionStats");

db.numbers.ensureIndex({ num: 1 });
db.numbers.getIndexes();


// 기본적인 관리
show dbs;
show collections;
db.stats();
db.numbers.stats();

// exam
use test;
for (let i = 0; i < 20000; i++) {
    db.product.insertOne({ num: i, name: "스마트폰 " + i });
};
db.product.count();

db.product.find()
    .sort({ num: -1 });
db.product.find()
    .sort({ num: -1 })
    .limit(10);
db.product.find()
    .sort({ num: -1 })
    .skip((6 - 1) * 10)
    .limit(10);

db.product.find({
    $or: [
        { num: { $lt: 15 } },
        { num: { $gt: 19995 } }
    ]
});
db.product.find({
    name: {
        $in: [
            "스마트폰 10", "스마트폰 100", "스마트폰 1000"
        ]
    }
});

db.product.find(
    { num: { $lt: 5 } },
    { name: 1, _id: 0 }
);

