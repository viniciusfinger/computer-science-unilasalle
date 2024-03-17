// Bruno Moretto e Vinicius Finger

const fs = require('fs');

const FILE_PATH = './listaFuncionarios.json';
const GENERATED_FILE_PATH = './funcionariosFiltrados.json';

const FEMALE_TYPE = 'M';
const MALE_TYPE = 'H';

getEmployeesData().then(employees => {
    const chineseFemaleEmployees = filterEmployeesByGenderAndCountry(employees, FEMALE_TYPE, 'China');
    const chineseFemaleEmployeeWithHighestSalary = getEmployeeWithHighestSalary(chineseFemaleEmployees);
    const chineseFemaleEmployeeWithLowerSalary = getEmployeesWithLowerSalary(chineseFemaleEmployees);

    const brazilianFemaleEmployees = filterEmployeesByGenderAndCountry(employees, FEMALE_TYPE, 'Brazil');
    const brazilianFemaleEmployeeWithHighestSalary = getEmployeeWithHighestSalary(brazilianFemaleEmployees);
    const brazilianFemaleEmployeeWithLowerSalary = getEmployeesWithLowerSalary(brazilianFemaleEmployees);

    const filteredEmployees = [
        chineseFemaleEmployeeWithHighestSalary,
        chineseFemaleEmployeeWithLowerSalary,
        brazilianFemaleEmployeeWithHighestSalary,
        brazilianFemaleEmployeeWithLowerSalary
    ];

    fs.writeFile(GENERATED_FILE_PATH, JSON.stringify(filteredEmployees), err => {
        err ? console.log('There was an error writing the file!')
            : console.log('File saved successfully!'); 
    });
});

async function getEmployeesData() { 
    const jsonData = await fs.promises.readFile(FILE_PATH, 'UTF-8');
    return JSON.parse(jsonData);
}

function filterEmployeesByGenderAndCountry(employees = [], gender, country) {
    return employees
        .filter(employee => employee.genero === gender)
        .filter(femaleEmployee => femaleEmployee.pais === country)
}

function getEmployeeWithHighestSalary(employees = []) {
    return employees.reduce(
        (employee1, employee2) => 
            employee1.salario > employee2.salario ? employee1 : employee2
        );
}

function getEmployeesWithLowerSalary(employees = []) {
    return employees.reduce(
        (employee1, employee2) => 
            employee1.salario < employee2.salario ? employee1 : employee2
        );
}

