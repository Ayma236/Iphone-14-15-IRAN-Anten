<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <!-- Cellular Settings -->
        <dict>
            <key>PayloadDisplayName</key>
            <string>Cellular</string>
            <key>PayloadIdentifier</key>
            <string>com.apple.cellular</string>
            <key>PayloadType</key>
            <string>com.apple.cellular</string>
            <key>PayloadUUID</key>
            <string>57c978ab-075e-48e0-bfb7-12ce76579b4e</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
            <key>APNs</key>
            <array>
                <!-- First APN -->
                <dict>
                    <key>AllowedProtocolMask</key>
                    <integer>3</integer>
                    <key>AllowedProtocolMaskInDomesticRoaming</key>
                    <integer>3</integer>
                    <key>AllowedProtocolMaskInRoaming</key>
                    <integer>3</integer>
                    <key>AuthenticationType</key>
                    <string>PAP</string>
                    <key>DefaultProtocolMask</key>
                    <integer>3</integer>
                    <key>EnableXLAT464</key>
                    <true />
                    <key>Name</key>
                    <string>mci-net</string>
                    <key>ProxyServer</key>
                    <string></string>
                    <key>Username</key>
                    <string></string>
                </dict>
                <!-- Second APN -->
                <dict>
                    <key>AllowedProtocolMask</key>
                    <integer>1</integer>
                    <key>AllowedProtocolMaskInDomesticRoaming</key>
                    <integer>1</integer>
                    <key>AllowedProtocolMaskInRoaming</key>
                    <integer>1</integer>
                    <key>AuthenticationType</key>
                    <string>CHAP</string>
                    <key>DefaultProtocolMask</key>
                    <integer>1</integer>
                    <key>EnableXLAT464</key>
                    <true />
                    <key>Name</key>
                    <string>mci-net</string>
                    <key>Username</key>
                    <string></string>
                </dict>
            </array>
            <key>AttachAPN</key>
            <dict>
                <key>AllowedProtocolMask</key>
                <integer>3</integer>
                <key>AuthenticationType</key>
                <string>PAP</string>
                <key>Name</key>
                <string>mci-net</string>
                <key>Username</key>
                <string></string>
            </dict>
        </dict>

        <!-- VPN Settings -->
        <dict>
            <key>PayloadDisplayName</key>
            <string>VPN</string>
            <key>PayloadIdentifier</key>
            <string>com.apple.vpn.managed.76a7c8d5-efd7-447a-9194-9f7b0ad603be</string>
            <key>PayloadType</key>
            <string>com.apple.vpn.managed</string>
            <key>PayloadUUID</key>
            <string>7ca66ffb-b3d7-4fc7-bca5-be006c551111</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
            <key>UserDefinedName</key>
            <string>VPN Configuration</string>
            <key>VPNType</key>
            <string>IPSec</string>
            <key>IPSec</key>
            <dict>
                <key>AuthenticationMethod</key>
                <string>SharedSecret</string>
                <key>ExtendedAuthEnabled</key>
                <false/>
                <key>LocalIdentifier</key>
                <string>mci-net</string>
                <key>RemoteAddress</key>
                <string>vpn.example.com</string>
                <key>SharedSecret</key>
                <string>0885235e-bc42-427a-a062-d74200380d11</string>
                <key>XAuthEnabled</key>
                <false/>
                <key>XAuthName</key>
                <string>mci-net</string>
                <key>XAuthPassword</key>
                <string>mci-net</string>
            </dict>
        </dict>

        <!-- Proxy Settings -->
        <dict>
            <key>PayloadDisplayName</key>
            <string>Proxy</string>
            <key>PayloadIdentifier</key>
            <string>com.apple.proxy.9d22c0bc-7fad-4a19-b86f-ed006681b2f7</string>
            <key>PayloadType</key>
            <string>com.apple.proxy</string>
            <key>PayloadUUID</key>
            <string>741adfa2-dadb-484f-9377-1e5e7d58f676</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
            <key>HTTPEnable</key>
            <true/>
            <key>HTTPPort</key>
            <integer>8080</integer>
            <key>HTTPSEnable</key>
            <true/>
            <key>HTTPSPort</key>
            <integer>8080</integer>
            <key>FTPEnable</key>
            <true/>
            <key>FTPPort</key>
            <integer>21</integer>
            <key>SOCKSEnable</key>
            <true/>
            <key>SOCKSPort</key>
            <integer>1080</integer>
            <key>Server</key>
            <string>proxy.example.com</string>
            <key>ExclusionList</key>
            <array>
                <string>localhost</string>
                <string>127.0.0.1</string>
                <string>169.254.0.0/16</string>
            </array>
        </dict>

        <!-- Additional Settings -->
        <dict>
            <key>PayloadDisplayName</key>
            <string>Additional Settings</string>
            <key>PayloadIdentifier</key>
            <string>com.example.additionalsettings.3355c33d-162a-46f8-bffa-730b8c719996</string>
            <key>PayloadType</key>
            <string>Configuration</string>
            <key>PayloadUUID</key>
            <string>80c59b20-63bd-4666-a1a4-2a3021734480</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
            <key>PayloadOrganization</key>
            <string>Github:AiGptCode</string>
            <key>PayloadRemovalDisallowed</key>
            <false/>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Configuration Profile</string>
    <key>PayloadIdentifier</key>
    <string>com.example.profile</string>
    <key>PayloadRemovalDisallowed</key>
    <false/>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>741adfa2-dadb-484f-9377-1e5e7d58f676</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
