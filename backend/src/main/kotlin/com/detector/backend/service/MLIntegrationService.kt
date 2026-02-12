//  futuramente o serviço é quem irá enviar o texto para o python e receber a resposta

package com.detector.backend.service

import org.springframework.stereotype.Service
import org.springframework.web.reactive.function.client.WebClient
import reactor.core.publisher.Mono

@Service
class MLIntegrationService(private val mlServiceWebClient: WebClient) {

    fun analyzeText(content: String): Mono<Map<*, *>> {
        val requestBody = mapOf("text" to content)

        return mlServiceWebClient.post()
            .uri("/predict") // Endpoint que será criado no Python
            .bodyValue(requestBody)
            .retrieve()
            .bodyToMono(Map::class.java)
    }

	//fun responseText(content: Srting){
	//	return mlServiceWebClient.get()
	//}
}