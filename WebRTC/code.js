let local_rtc = new RTCPeerConnection();
let remote_rtc = new RTCPeerConnection();

local_rtc.onicecandidate = e => {
	if(e.candidate){
		remote_rtc.addIceCandidate(e.candidate)
	}
}
remote_rtc.onicecandidate = e => {
	if(e.candidate){
		local_rtc.addIceCandidate(e.candidate)
	}
}
navigator.mediaDevices.getUserMedia({
	video:true
}).then(stream => {
	document.getElementById("local").srcObject = stream;
	local_rtc.addStream(stream);
	return local_rtc.createOffer();
}).then(offer => {
	return local_rtc.setLocalDescription(new RTCSessionDescription(offer))
}).then(() => {
	return remote_rtc.setRemoteDescription(local_rtc.localDescription)
}).then(() => {
	return remote_rtc.createAnswer()
}).then(answer => {
	return remote_rtc.setLocalDescription(new RTCSessionDescription(answer))
}).then(() => {
	console.log(remote_rtc.localDescription)
	return local_rtc.setRemoteDescription(remote_rtc.localDescription)
})

remote_rtc.ontrack = e => {
	document.getElementById("remote").srcObject = e.streams[0]
}