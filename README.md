# OnDemand/Passenger: Flask + Vue example app

## Vue

```
npm create vue@latest
```

Move to project folder
```
npm install
```

Change `vite.config.js` to remove hash from build filenames:
```
  build: {
    rollupOptions: {
      output: {
        entryFileNames: `assets/[name].js`,
        chunkFileNames: `assets/[name].js`,
        assetFileNames: `assets/[name].[ext]`
      }
    }
  }
  ```

Build
```
npm run build
```

## Flask

### Install pyslurm

Need to build ?

