module.exports = {
    flowFile: 'flows.json',
    flowFilePretty: true,
    uiPort: process.env.PORT || 1880,
    logging: {
        console: {
            level: "info",
            metrics: false,
            audit: false
        }
    },
    exportGlobalContextKeys: false,
    externalModules: {},
    editorTheme: {
        palette: {},
        projects: {
            enabled: true,
            workflow: {
                mode: "manual"
            }
        },
        codeEditor: {
            lib: "ace",
            options: {
                theme: "vs",
            }
        }
    },
    functionExternalModules: true,
    functionGlobalContext: {
    },
    debugMaxLength: 1000,
    mqttReconnectTime: 15000,
    serialReconnectTime: 15000,
    contextStorage: {
        default: "file",
        memoryOnly: { module: 'memory' },
        file: { module: 'localfilesystem' }
    }
}
