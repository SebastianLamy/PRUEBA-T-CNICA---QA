import http from 'k6/http';
import { check } from 'k6';
export let options = {
vus: 50,
duration: '1m',
};
export default function () {
let res = http.get('https://reqres.in/api/users');
9
check(res, { 'status 200': (r) => r.status === 200 });
}