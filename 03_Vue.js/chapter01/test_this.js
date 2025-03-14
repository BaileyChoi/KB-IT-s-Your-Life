const obj1 = {
	name: "홍길동",
	getName() {
		console.log(this.name);
	},
};
obj1.getName();

const obj2 = {
	name: "홍길동",
	getName() {
		console.log(this.name);
	},
};
const irum1 = obj2.getName;
irum1();

const obj3 = {
	name: "홍길동",
	getName() {
		console.log(this.name);
	},
};
const irum2 = obj3.getName.bind(obj3); //bind는 this를 찾아주는 역활을 한다.
irum2();

const obj4 = {
	name: "홍길동",
	getName() {
		console.log(this.name);
	},
	obj5: {
		age: 25,
		getAge() {
			console.log(this.age);
		},
	},
};
const irum3 = obj4.getName.bind(obj4); //bind는 this를 찾아주는 역활을 한다.
irum3();
const nai = obj4.obj5.getAge.bind(obj4.obj5);
nai();
