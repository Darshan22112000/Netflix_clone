// This file can be replaced during build by using the `fileReplacements` array.
// `ng build --prod` replaces `environment.ts` with `environment.prod.ts`.
// The list of file replacements can be found in `angular.json`.

export const environment = {
  production: false,
  serverUrl: 'http://localhost:8000',
  socketConfig: {
    url: 'http://localhost:3005',
    options: {},
  },
  showTeamLogos: true,
  ssoEnabled: false,
  context_root: '',
  msalEnabled: false,
  msalClient: '',
  msalTenant: '',
  msalRedirectUrl: '',
  dpt_download_upload_timeout: 900000,
  stat_download_upload_timeout: 900000,
  environmentMessage: 'User Testing Version',
  // bayer_goc_url: 'http://bayer-prod-ey-951747631.us-east-1.elb.amazonaws.com:4446/joc/',
  bayer_goc_url: `http://${window.location.hostname}:4446/joc/`,
};
/*
 * For easier debugging in development mode, you can import the following file
 * to ignore zone related error stack frames such as `zone.run`, `zoneDelegate.invokeTask`.
 *
 * This import should be commented out in production mode because it will have a negative impact
 * on performance if an error is thrown.
 */
// import 'zone.js/plugins/zone-error';  // Included with Angular CLI.
