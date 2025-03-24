function makeStudent(name, korean, math, english, science) {
	let student = {
		name: name,
		korean: korean,
		math: math,
		english: english,
		science: science,
		getSum: function () {
			return this.korean + this.math + this.english + this.science;
		},
		getAverage: function () {
			return this.getSum() / 4;
		},
		toString: function () {
			return `${this.name}\t${this.getSum()}\t\t${this.getAverage()}`;
		},
	};
	return student;
}

let students = [];
students.push(makeStudent("윤인성", 90, 83, 76, 89));
students.push(makeStudent("박찬호", 90, 83, 76, 89));
students.push(makeStudent("류현진", 90, 83, 76, 89));
students.push(makeStudent("이세돌", 90, 83, 76, 89));
students.push(makeStudent("김세진", 90, 83, 76, 89));
students.push(makeStudent("이하나", 90, 83, 76, 89));

let output = "name\t총점\t평균\n";

for (let i in students) {
	output += students[i].toString() + "\n";
}

console.log(output);
