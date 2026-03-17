FROM eclipse-temurin:17-jdk

WORKDIR /app

# copia o jar gerado
COPY build/libs/*.jar app.jar

EXPOSE 8080

ENTRYPOINT ["java","-jar","app.jar"]