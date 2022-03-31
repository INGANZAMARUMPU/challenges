package bi.hogi.inganzamarumpu;

import android.content.Intent;
import android.widget.Toast;

import androidx.activity.result.ActivityResult;

import com.getcapacitor.JSObject;
import com.getcapacitor.Plugin;
import com.getcapacitor.PluginCall;
import com.getcapacitor.PluginMethod;
import com.getcapacitor.annotation.ActivityCallback;
import com.getcapacitor.annotation.CapacitorPlugin;


@CapacitorPlugin(name = "QrScanner")
public class Plugins extends Plugin {

    @PluginMethod()
    public void startScan(PluginCall call) {
        Intent intent = new Intent(getContext(), ScannerActity.class);
        startActivityForResult(call, intent, "onQrScanResult");
    }

    @ActivityCallback
    public void onQrScanResult(PluginCall call, ActivityResult result){
        if (call == null) {
            Toast.makeText(getContext(), "Scan Cancelled", Toast.LENGTH_LONG).show();
            return;
        }
        JSObject ret = new JSObject();
        ret.put("value", result.getData().getStringExtra("found"));
        call.resolve(ret);
    }
}