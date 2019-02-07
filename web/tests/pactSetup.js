import path from 'path';
import { Pact } from '@pact-foundation/pact'

global.port = 5000;
global.provider = new Pact({
  port: global.port,
  log: path.resolve(process.cwd(), 'logs', 'mockserver-integration.log'),
  dir: path.resolve(process.cwd(), 'pacts'),
  spec: 2,
  cors: true,
  pactfileWriteMode: 'update',
  consumer: 'Front-end Vue SPA',
  provider: 'Back-end API'
});
