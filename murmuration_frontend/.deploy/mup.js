module.exports = {
  servers: {
    one: {
      // TODO: set host address, username, and authentication method
      host: '54.144.163.235',
      username: 'ubuntu',
      pem: '~/.ssh/murmurationZahn.pem',
      // password: 'server-password'
      // or neither for authenticate from ssh-agent
    }
  },

  app: {
    // TODO: change app name and path
    name: 'murmuration_frontend',
    path: '../',

    servers: {
      one: {},
    },

    buildOptions: {
      serverOnly: true,
    },

    env: {
      // TODO: Change to your app's url
      // If you are using ssl, it needs to start with https://
      ROOT_URL: 'http://www.murmuration-taxi.com',
      MONGO_URL: 'mongodb://meteor:lostStarling@ec2-34-227-52-163.compute-1.amazonaws.com:27017/meteor',
    },
		deployCheckWaitTime: 40,

    // ssl: { // (optional)
    //   // Enables let's encrypt (optional)
    //   autogenerate: {
    //     email: 'email.address@domain.com',
    //     // comma separated list of domains
    //     domains: 'website.com,www.website.com'
    //   }
    // },

    docker: {
      // change to 'abernix/meteord:base' if your app is using Meteor 1.4 - 1.5
      image: 'abernix/meteord:node-8.4.0-base',
    },

    // Show progress bar while uploading bundle to server
    // You might need to disable it on CI servers
    enableUploadProgressBar: true
  },

  proxy: {
    domains: 'www.murmuration-taxi.com',
    ssl: {
      // Enable let's encrypt to create free certificates
      letsEncryptEmail: 'mike@fare-taxi.com',
			forceSSL: true
    }
  }
};
