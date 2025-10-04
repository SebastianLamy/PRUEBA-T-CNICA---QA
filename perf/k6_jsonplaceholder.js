import http from 'k6/http';
import { sleep, check } from 'k6';
export let options = {
vus: 100,
duration: '2m',
};
export default function () {
let res = http.get('https://jsonplaceholder.typicode.com/posts');
check(res, {
'status 200': (r) => r.status === 200,
'response < 2s': (r) => r.timings.duration < 2000
});
sleep(1);
}