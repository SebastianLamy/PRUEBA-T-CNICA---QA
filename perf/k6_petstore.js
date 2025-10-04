import http from 'k6/http';
import { check, sleep } from 'k6';
export let options = {
vus: 10,
duration: '6m',
rps: 200
};
export default function () {
let res = http.get('https://petstore.swagger.io/v2/pet/findByStatus?status=available');
check(res, { 'status 200': (r) => r.status === 200 });
sleep(1);
}