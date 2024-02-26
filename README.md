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

Use python in `/usr/bin/python`



```
conda deactivate
cd /home/users/f/ferat/Documents/GitHub
git clone https://github.com/PySlurm/pyslurm.git
cd pyslurm

pip-3.6 install cython --user

/usr/bin/python setup.py build
/usr/bin/python setup.py install --user
```

iF VERSION ERROR:
```
/usr/bin/pip-3.6 install -U packaging --user
```

